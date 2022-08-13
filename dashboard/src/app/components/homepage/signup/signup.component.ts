import { Component, OnInit, ViewChild } from '@angular/core';
import { RequestsService } from '../../../services/requests.service';
import { Router } from '@angular/router';
import { GooglePlaceDirective } from "ngx-google-places-autocomplete";
import { Address } from 'ngx-google-places-autocomplete/objects/address';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})

export class SignupComponent implements OnInit {

  private nonWhitespaceRegExp: RegExp = new RegExp("[a-zA-Z0-9]");
  public registerForm: FormGroup = this.fb.group({
    firstName: ['', [Validators.required]],
    lastName: ['', [Validators.required]],
    address: ['', [Validators.required]],
    city: "",
    state: "",
    country: "",
    postal: "",
    phone: ['', [Validators.required, Validators.minLength(10)]],
    email: ['', [Validators.required, Validators.email]],
    username: ['', [Validators.required, Validators.minLength(10), this.noWhiteSpace]],
    password: ['', [Validators.required, Validators.minLength(8)]],
    password1: ['', [Validators.required, Validators.minLength(8)]]
  });


  private countries = { 'US': "USA", 'CA': "Canada" }

  public user = {
    firstName: "",
    lastName: "",
    address: "",
    city: "",
    state: "",
    country: "",
    postal: "",
    phone: "",
    email: "",
    password: "",
    username: "",
  }

  constructor(private _requests: RequestsService, private router: Router, private fb: FormBuilder) { }

  ngOnInit(): void { }

  public get firstName(): any { return this.registerForm.get('firstName'); }
  public get lastName(): any { return this.registerForm.get('lastName'); }
  public get address(): any { return this.registerForm.get('address'); }
  public get email(): any { return this.registerForm.get('email'); }
  public get phone(): any { return this.registerForm.get('phone'); }
  public get username(): any { return this.registerForm.get('username'); }
  public get password(): any { return this.registerForm.get('password'); }
  public get password1(): any { return this.registerForm.get('password1'); }

  public noWhiteSpace(control) {
    console.log(control)
    if ((control.value).indexOf(' ') >= 0) {
      return { cannotContainSpace: true };
    }

    return null;
  }

  registerFormSubmit(): void {
    // const formData = this.registerForm.value;
    // delete formData.password1;
    // console.log(formData);
    // this.signup()
  }

  public handleAddressChange(address) {
    this.user.address = address.formatted_address;
    for (var a of address.address_components) {
      if (a.types.includes("locality")) {
        this.user.city = a.long_name
      }

      if (a.types.includes("administrative_area_level_1")) {
        this.user.state = a.long_name
      }

      if (a.types.includes("country")) {
        this.user.country = a.short_name
      }

      if (a.types.includes("postal_code")) {
        this.user.postal = a.long_name
      }
    }

    if (this.user.country in this.countries) {
      this.user.country = this.countries[this.user.country]
    } else {
      this.user.state = "";
    }
  }

  public signup() {

    this.user['email'] = this.registerForm.value['email'];
    this.user['firstName'] = this.registerForm.value['firstName'];
    this.user['lastName'] = this.registerForm.value['lastName'];
    this.user['password'] = this.registerForm.value['password'];
    this.user['phone'] = this.registerForm.value['phone'];
    this.user['username'] = this.registerForm.value['username'];

    this._requests.postRequest("signup", this.user).subscribe(res => {
      if (res['status'] == 200) {
        this.router.navigateByUrl("/login");
      }
      console.log(res)
    }, err => {
      console.log(err)
    });
  }

}
