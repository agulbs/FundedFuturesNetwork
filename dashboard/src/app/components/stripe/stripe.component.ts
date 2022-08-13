import { Component, OnInit } from '@angular/core';
import { Stripe } from "stripe-angular";

@Component({
  selector: 'app-stripe',
  templateUrl: './stripe.component.html',
  styleUrls: ['./stripe.component.css']
})
export class StripeComponent implements OnInit {
  public stripe;
  public card;

  constructor() { }

  ngOnInit(): void {
  }

  public configureStripe() {
    this.stripe = Stripe('pk_test_51LVNKPKSvK2NDY9DlJ0Rk1sHelqPhWFoufs4oiglsVANLWDoDk7AaFsunqsLoGpm1kIof6Z61UPTUtxqrPSliU8w00Elkoisnb');

    // const style = {
    //   base: {
    //     color: '#32325d',
    //     fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    //     fontSmoothing: 'antialiased',
    //     fontSize: '16px',
    //     '::placeholder': {
    //       color: '#aab7c4'
    //     },
    //     backgroundColor: "black",
    //   },
    //   invalid: {
    //     color: '#fa755a',
    //     iconColor: '#fa755a'
    //   },
    // };
    //
    // const appearance = { theme: "night", labels: "floating" }
    //
    // this.stripe = Stripe('pk_test_51LVNKPKSvK2NDY9DlJ0Rk1sHelqPhWFoufs4oiglsVANLWDoDk7AaFsunqsLoGpm1kIof6Z61UPTUtxqrPSliU8w00Elkoisnb');
    // console.log(this.stripe)
    // const elements = this.stripe.elements();
    // this.card = elements.create('card', { style: style });
    // // this.card.mount('#card-element');
    //
    // this.card.addEventListener('change', (event) => {
    //   if (event.error) {
    //     console.log(event.error)
    //   } else {
    //   }
    // });

  }

  // public createToken() {
  //
  //   this.stripe.createToken(this.card).then((result) => {
  //     console.log(result)
  //     if (result.error) {
  //
  //     } else {
  //       result['user'] = this._state.user;
  //       result['user']['cash'] = this.selectedTier['equity']
  //       result['user']['tier'] = this.selectedTier['id']
  //       result['user']['reset'] = this._state.user['ffn'] != null
  //       result['purchase'] = this.selectedTier
  //       console.log(result)
  //       this._requests.postRequest("checkout", result).subscribe(res => {
  //         console.log(res)
  //       })
  //     }
  //   });
  // };
  //
  //
  // public purchase(tier) {
  //   const params = {
  //     user: this._state.user,
  //     cash: tier['equity'],
  //     ffn: this._state.user['ffn'],
  //     tier: tier['id'],
  //     reset: this._state.user['ffn'] != null,
  //   }
  //
  //   this._requests.postRequest("user/purchase-membership", params).subscribe(res => {
  //     if (res['status'] == 200) {
  //       this._state.user['tier'] = tier['id'];
  //       this._state.user['friendly'] = tier['friendly'];
  //       this._state.user['price'] = tier['price'];
  //       this._state.setUser(this._state.user);
  //     }
  //   })
  // }

}
