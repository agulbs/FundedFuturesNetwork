import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { StateService } from '../../services/state.service';


@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

  constructor(private router: Router, private _state: StateService) {

  }

  ngOnInit(): void {
    var user = localStorage.getItem('ffn');
    if (user) {
      user = JSON.parse(user);
      this.router.navigateByUrl('dashboard');
      this._state.setUser(user);
    }
  }

}
