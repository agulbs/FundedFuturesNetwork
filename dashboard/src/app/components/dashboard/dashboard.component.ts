import { Component, OnInit } from '@angular/core';
import { StateService } from '../../services/state.service';
import { RequestsService } from '../../services/requests.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  public user;

  constructor(private _state: StateService, private _requests: RequestsService, ) {

  }

  ngOnInit(): void {
    this.getUserInfo()
  }

  public getUserInfo() {
    console.log(this._state.user)
    this._requests.postRequest("user", { 'user': this._state.user['username'] }, this._state.user).subscribe(res => {
      if (res['status'] == 200) {
        this._state.setUser(res['message'])
      } else {

      }
    })
  }

}
