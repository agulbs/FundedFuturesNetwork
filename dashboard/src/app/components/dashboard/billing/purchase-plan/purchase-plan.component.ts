import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../../services/requests.service'
import { StateService } from '../../../../services/state.service'
import { Router } from '@angular/router';

@Component({
  selector: 'app-purchase-plan',
  templateUrl: './purchase-plan.component.html',
  styleUrls: ['./purchase-plan.component.css']
})
export class PurchasePlanComponent implements OnInit {
  public tiers = [];

  constructor(private _requests: RequestsService, private _state: StateService, private router: Router) { }

  ngOnInit(): void {
    this._requests.getRequest("tiers").subscribe(res => {
      if (res['status'] == 200) {
        this.tiers = res['message']
      }
    })
  }

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
