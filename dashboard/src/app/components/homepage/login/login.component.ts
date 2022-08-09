import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../services/requests.service';
import { StateService } from '../../../services/state.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public user = {
    username: "",
    password: ""
  }

  constructor(private _requests: RequestsService, private _state: StateService, private router: Router) { }

  ngOnInit(): void {
  }

  public login() {

    this._requests.postRequest("login", this.user).subscribe(res => {
      if (res['status'] == 200) {
        this._state.setUser(this.user);
        this.router.navigateByUrl("/dashboard");
      } else {
        alert(res['message'])
      }
    })
  }

}
