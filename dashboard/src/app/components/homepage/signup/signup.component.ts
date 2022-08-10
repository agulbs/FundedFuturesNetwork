import { Component, OnInit, ViewChild } from '@angular/core';
import { RequestsService } from '../../../services/requests.service';
import { Router } from '@angular/router';
import { GooglePlaceDirective } from "ngx-google-places-autocomplete";
import { Address } from 'ngx-google-places-autocomplete/objects/address';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})

export class SignupComponent implements OnInit {
  // @ViewChild("placesRef") placesRef: GooglePlaceDirective;

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

  constructor(private _requests: RequestsService, private router: Router) { }

  ngOnInit(): void {
  }

  public handleAddressChange(address) {
    console.log(address)
    this.user.address = address.formatted_address;
    for (var a of address.address_components) {
      console.log(a)
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
    console.log(this.user);

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
