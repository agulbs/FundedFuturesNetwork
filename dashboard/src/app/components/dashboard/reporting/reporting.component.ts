import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../services/requests.service';
import { StateService } from '../../../services/state.service';

@Component({
  selector: 'app-reporting',
  templateUrl: './reporting.component.html',
  styleUrls: ['./reporting.component.css']
})
export class ReportingComponent implements OnInit {
  public user = {};

  constructor(private _requests: RequestsService, private _state: StateService) {
    this._state.userBehavoirSubject.subscribe(res => {
      if ('tier' in res) {
        this.user = res
      }
    })
  }

  ngOnInit(): void {
    // console.log(this._state.user)
    // this._requests.postRequest("reporting", { user: this._state.user['username'] }).subscribe(res => {
    //   if (res['status'] == 200) {
    //     this._state.setUser(res['message']);
    //     console.log(this._state.user)
    //   }
    // })

  }

}
