import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../services/requests.service'
import { StateService } from '../../../services/state.service'

@Component({
  selector: 'app-invoice',
  templateUrl: './invoice.component.html',
  styleUrls: ['./invoice.component.css']
})
export class InvoiceComponent implements OnInit {

  public invoices = []

  constructor(private _requests: RequestsService, private _state: StateService) {
    this._state.userBehavoirSubject.subscribe(user => {
      if (Object.keys(user).length > 0) {
        this.getInvoices(user);
      }
    })
  }

  ngOnInit(): void { }


  public getInvoices(user) {
    console.log(user)
    this._requests.postRequest("user/invoices", { 'username': user['username'] }, user).subscribe(res => {
      console.log(res)
      if (res['status'] == 200) {
        this.invoices = res['message'];
        console.log(this.invoices)
      }
    })
  }
}
