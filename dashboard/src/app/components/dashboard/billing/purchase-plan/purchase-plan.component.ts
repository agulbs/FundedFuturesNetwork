import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../../services/requests.service'
import { StateService } from '../../../../services/state.service'
import { PaymentService } from '../../../../services/payment.service'
import { Router } from '@angular/router';
import { Stripe } from "stripe-angular"
import { GooglePlaceDirective } from "ngx-google-places-autocomplete";
import { Address } from 'ngx-google-places-autocomplete/objects/address';


@Component({
  selector: 'app-purchase-plan',
  templateUrl: './purchase-plan.component.html',
  styleUrls: ['./purchase-plan.component.css']
})
export class PurchasePlanComponent implements OnInit {
  private countries = { 'US': "USA", 'CA': "Canada" }
  public tiers = [];
  public selectedTier = {};
  public user = {}
  public affiliateCode = "";
  public discount = 0;

  public stripe;
  public card;
  public displayError = "";

  constructor(
    private _requests: RequestsService,
    private _state: StateService,
    private _payment: PaymentService,
    private router: Router
  ) {
    this._state.userBehavoirSubject.subscribe(user => {
      if (Object.keys(user).length > 0) {
        this.user = user;
        console.log(user)
      }
    })
  }

  ngOnInit(): void {
    this.configureStripe();
    this._requests.getRequest("tiers").subscribe(res => {
      if (res['status'] == 200) {
        this.tiers = res['message']
      }
    })

  }

  public setSelectedTier(tier, plan) {
    this.selectedTier = tier;
    if (plan == 0) {
      this.selectedTier['package'] = "Standard Package"
      this.selectedTier['status'] = "S"
      this.selectedTier['price'] = tier['standardPrice'];
      this.selectedTier['total'] = tier['standardPrice'];
    } else {
      this.selectedTier['package'] = "Express Package"
      this.selectedTier['status'] = "E"
      this.selectedTier['price'] = tier['expressPrice'];
      this.selectedTier['total'] = tier['expressPrice'];
    }

    this.user = {};
    this.user = this._state.user;
  }

  public handleAddressChange(address) {
    console.log(address)
    this._state.user['address'] = address.formatted_address;
    for (var a of address.address_components) {
      console.log(a)
      if (a.types.includes("locality")) {
        this._state.user['city'] = a.long_name
      }

      if (a.types.includes("administrative_area_level_1")) {
        this._state.user['state'] = a.long_name
      }

      if (a.types.includes("country")) {
        this._state.user['country'] = a.short_name
      }

      if (a.types.includes("postal_code")) {
        this._state.user['postal'] = a.long_name
      }
    }

    if (this._state.user['country'] in this.countries) {
      this._state.user['country'] = this.countries[this._state.user['country']]
    } else {
      this._state.user['state'] = "";
    }
  }

  public configureStripe() {
    const style = {
      theme: "night",
      base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
          color: '#aab7c4'
        },
        background: "red",
      },
      invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
      }
    };

    const appearance = { theme: "night", labels: "floating" }

    this.stripe = Stripe('pk_test_51LVNKPKSvK2NDY9DlJ0Rk1sHelqPhWFoufs4oiglsVANLWDoDk7AaFsunqsLoGpm1kIof6Z61UPTUtxqrPSliU8w00Elkoisnb');
    console.log(this.stripe)
    const elements = this.stripe.elements();
    this.card = elements.create('card', { style: style });
    this.card.mount('#card-element');


    this.card.addEventListener('change', (event) => {
      if (event.error) {
        console.log(event.error)
        this.displayError = event.error.message;
      } else {
        this.displayError = ''
      }
    });

  }

  public applyAffiliateDiscount() {
    if (this.affiliateCode.length < 0) {
      this.discount = 0;
      return;
    }
    const params = { user: this._state.user, affiliateCode: this.affiliateCode }
    this._requests.postRequest("checkout/apply-discount", params).subscribe(res => {
      if (res['status'] == 200) {
        this.discount = this.selectedTier['price'] * res['message'][0]['discount'];
        this.selectedTier['total'] = this.selectedTier['price'] - this.discount;
        this.selectedTier['affiliateCode'] = this.affiliateCode
      }
    })
  }

  public createToken() {

    this.stripe.createToken(this.card).then((result) => {
      console.log(result)
      if (result.error) {

      } else {
        result['user'] = this._state.user;
        result['user']['cash'] = this.selectedTier['equity']
        result['user']['tier'] = this.selectedTier['id']
        result['user']['reset'] = this._state.user['ffn'] != null
        result['purchase'] = this.selectedTier
        result['purchase']['price'] = result['purchase']['total']
        console.log(result)
        this._requests.postRequest("checkout", result).subscribe(res => {
          console.log(res)
        })
      }
    });
  };


  public purchase(tier) {
    const params = {
      user: this._state.user,
      cash: tier['equity'],
      ffn: this._state.user['ffn'],
      tier: tier['id'],
      reset: this._state.user['ffn'] != null,
    }

    this._requests.postRequest("user/purchase-membership", params).subscribe(res => {
      if (res['status'] == 200) {
        this._state.user['tier'] = tier['id'];
        this._state.user['friendly'] = tier['friendly'];
        this._state.user['price'] = tier['price'];
        this._state.setUser(this._state.user);
        this.router.navigateByUrl("../dashboard")
      }
    })
  }

}
