import { Component, OnInit } from '@angular/core';
import { StateService } from '../../../../services/state.service';
import { RequestsService } from '../../../../services/requests.service';
@Component({
  selector: 'app-membership',
  templateUrl: './membership.component.html',
  styleUrls: ['./membership.component.css']
})
export class MembershipComponent implements OnInit {

  public user = {};
  public memberships = [];

  constructor(private _state: StateService, private _requests: RequestsService) {
    this._state.userBehavoirSubject.subscribe(user => {
      if ('tier' in user) {
        this.user = user;
        this.getMemberships()
      }
    })
  }

  ngOnInit(): void {
    console.log(this.user)

  }

  public getMemberships() {
    this._requests.postRequest("user/memberships", { username: this.user['username'] }, this.user).subscribe(res => {
      console.log(res)
      if (res['status'] == 200) {
        console.log(res)
        this.memberships = res['message'];
      }
    })
  }

}
