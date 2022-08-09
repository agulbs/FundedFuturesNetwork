import { Component, OnInit } from '@angular/core';
import { StateService } from '../../services/state.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(private _state: StateService) {

  }

  ngOnInit(): void {
    var user = localStorage.getItem('ffn');
    if (user) {
      user = JSON.parse(user);
      console.log(user)
      this._state.setUser(user);
    }
  }

}
