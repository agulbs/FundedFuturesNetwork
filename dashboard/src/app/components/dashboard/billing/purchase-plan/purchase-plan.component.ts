import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../../services/requests.service'
import { StateService } from '../../../../services/state.service'
import { PaymentService } from '../../../../services/payment.service'
import { Router } from '@angular/router';
import { Stripe } from "stripe-angular"


@Component({
  selector: 'app-purchase-plan',
  templateUrl: './purchase-plan.component.html',
  styleUrls: ['./purchase-plan.component.css']
})
export class PurchasePlanComponent implements OnInit {
  public tiers = [];
  public selectedTier = {};

  public stripe;
  public card;

  constructor(
    private _requests: RequestsService,
    private _state: StateService,
    private _payment: PaymentService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.configureStripe();

    this._requests.getRequest("tiers").subscribe(res => {
      if (res['status'] == 200) {
        res['message'].forEach(tier => {
          tier['description'] = tier['description'].split('~')
        })
        this.tiers = res['message']
      }
    })

  }

  public configureStripe() {
    const style = {
      base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
          color: '#aab7c4'
        }
      },
      invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
      }
    };

    this.stripe = Stripe('pk_test_51LVNKPKSvK2NDY9DlJ0Rk1sHelqPhWFoufs4oiglsVANLWDoDk7AaFsunqsLoGpm1kIof6Z61UPTUtxqrPSliU8w00Elkoisnb');
    console.log(this.stripe)
    const elements = this.stripe.elements();
    this.card = elements.create('card', { style: style });
    this.card.mount('#card-element');

    this.card.addEventListener('change', (event) => {
      if (event.error) {
        console.log(event.error)
      } else {
      }
    });

  }

  public createToken() {

    this.stripe.createToken(this.card).then((result) => {
      console.log(result)
      if (result.error) {

      } else {
        result['user'] = this._state.user;
        result['purchase'] = this.selectedTier
        this._requests.postRequest("checkout", result).subscribe(res => {
          console.log(res)
        })
      }
    });
  };


  public purchase(tier) {
    const params = {
      user: this._state.user['username'],
      username: this._state.user['username'],
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
      }
    })
  }

}
