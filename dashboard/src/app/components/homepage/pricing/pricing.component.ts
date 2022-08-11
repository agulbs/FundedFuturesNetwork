import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../services/requests.service'
@Component({
  selector: 'app-pricing',
  templateUrl: './pricing.component.html',
  styleUrls: ['./pricing.component.css']
})
export class PricingComponent implements OnInit {
  public tiers = [];
  constructor(private _requests: RequestsService) { }

  ngOnInit(): void {
    this._requests.getRequest("tiers").subscribe(res => {
      if (res['status'] == 200) {
        this.tiers = res['message']
      }
    })
  }

}
