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
  public accountBalance = {
    balance: 0,
    pnl: 0,
    threshold: 0,
  }

  constructor(private _requests: RequestsService, private _state: StateService) {
    this._state.userBehavoirSubject.subscribe(res => {
      console.log(res)
      if ('tier' in res) {
        this.user = res
        this.getAccountBalance();
      }
    })
  }

  ngOnInit(): void {
  }

  public getAccountBalance() {
    const params = { 'acct': this.user['ffn'] };
    this._requests.customPost("https://fundedfuturesnetwork.com/ftp/", params).subscribe(res => {
      const accountBalance = Number(res['Account Balance']);
      const cashOnHand = Number(res['Cash On Hand (Previous EOD)']);
      const threshold = Number(res["Auto Liquidate Threshold Value"]);

      this.accountBalance.balance = accountBalance;
      this.accountBalance.pnl = accountBalance - cashOnHand;
      this.accountBalance.threshold = threshold;


      console.log(res)
    })
  }

}
