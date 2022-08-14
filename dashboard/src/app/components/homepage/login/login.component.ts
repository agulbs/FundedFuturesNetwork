import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../services/requests.service';
import { StateService } from '../../../services/state.service';
import { AuthService } from '../../../services/auth.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public loginForm: FormGroup = this.fb.group({
    username: ['', [Validators.required]],
    password: ['', [Validators.required]],
  });

  public user = {
    username: "",
    password: ""
  }

  constructor(
    private _requests: RequestsService,
    private _state: StateService,
    private _auth: AuthService,
    private router: Router,
    private fb: FormBuilder
  ) { }

  ngOnInit(): void {
    if (this._state.user) {
      this.router.navigateByUrl("/dashboard")
    }
  }

  public get username(): any { return this.loginForm.get('username'); }
  public get password(): any { return this.loginForm.get('password'); }

  public loginFormSubmit(): void {
  }

  public login() {
    this.user = {
      username: this.loginForm.value['username'],
      password: this.loginForm.value['password'],
    }

    this._requests.postRequest("login", this.user, this.user).subscribe(res => {
      console.log(res)
      if (res['status'] == 200) {
        this.user['token'] = res['message']
        this._auth.userSubject.next(this.user);
        this._state.setUser(this.user);
        this.router.navigateByUrl("/dashboard");
      } else {
        alert(res['message'])
      }
    })
  }

}
