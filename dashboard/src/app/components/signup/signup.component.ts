import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../services/requests.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})

export class SignupComponent implements OnInit {
  public user = {
    firstName: "",
    lastName: "",
    address: "",
    phone: "",
    email: "",
    password: "",
  }

  constructor(private _requests: RequestsService, private router: Router) { }

  ngOnInit(): void {
  }

  public signup() {
    console.log(this.user);

    this._requests.postRequest("signup", this.user).subscribe(res => {
      if (res['staus'] == 200) {
        this.router.navigateByUrl("/login");
      }
      console.log(res)
    }, err => {
      console.log(err)
    });
  }

}
