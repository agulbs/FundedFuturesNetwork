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
    this._state.userBehavoirSubject.subscribe(user => {
      if (Object.keys(user).length == 0) { return; }
    })
  }

  ngOnInit(): void {
    var user = localStorage.getItem('ffn');

    if (user) {
      console.log(user)
      this.saveUser(JSON.parse(user));
    } else {
      alert("REROUTE")
    }
  }

  public saveUser(user) {
    this._requests.postRequest("user", { 'user': user['username'] }).subscribe(res => {
      console.log(res)
      if (res['status'] == 200) {
        this._state.setUser(res['message']);
        this.user = res['message'];
      }
    })
  }

}
