import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../services/requests.service'
import { StateService } from '../../../services/state.service'
import { GooglePlaceDirective } from "ngx-google-places-autocomplete";
import { Address } from 'ngx-google-places-autocomplete/objects/address';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  public user = {}
  private countries = { 'US': "USA", 'CA': "Canada" }

  constructor(private _state: StateService, private _requests: RequestsService) {
    this._state.userBehavoirSubject.subscribe(user => {
      this.user = JSON.parse(JSON.stringify(user))
    })
  }

  ngOnInit(): void {
  }

  public handleAddressChange(address) {
    console.log(address)
    this.user['address'] = address.formatted_address;
    for (var a of address.address_components) {
      console.log(a)
      if (a.types.includes("locality")) {
        this.user['city'] = a.long_name
      }

      if (a.types.includes("administrative_area_level_1")) {
        this.user['state'] = a.long_name
      }

      if (a.types.includes("country")) {
        this.user['country'] = a.short_name
      }

      if (a.types.includes("postal_code")) {
        this.user['postal'] = a.long_name
      }
    }

    if (this.user['country'] in this.countries) {
      this.user['country'] = this.countries[this.user['country']]
    } else {
      this.user['state'] = "";

    }
  }

  public update() {
    ["accountCreated", "dateSubscribed", "equity", "ffn", "friendly", "tier"].forEach(k => {
      delete this.user[k]
    })

    var flag = false;
    for (var key of Object.keys(this.user)) {
      if (this.user[key] != this._state.user[key]) {
        flag = true;
        break;
      }
    }

    if (flag) {
      this._requests.postRequest("user/update", this.user).subscribe(res => {
        console.log(res)
      })
    }

  }

}
