import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { RequestsService } from '../../../services/requests.service';
import { StateService } from '../../../services/state.service';
import Swal from 'ngx-angular8-sweetalert2'



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

  public resetFlag = false;

  constructor(private _requests: RequestsService, private _state: StateService, private router: Router) {
    this._state.userBehavoirSubject.subscribe(res => {
      if (Object.keys(res).length > 0 && 'tier' in res) {
        this.user = res;
        console.log(this.user)
        this.getAccountBalance();
      }
    })
  }

  ngOnInit(): void {
  }

  public getAccountBalance() {

    const params = { 'acct': this.user['ffn'] };
    // const params = { 'acct': "FFN-48500878" };
    this._requests.customPost("https://fundedfuturesnetwork.com/ftp/", params).subscribe(res => {
      console.log(res)
      if (Object.keys(res).length == 0) {
        return;
      }

      const accountBalance = Number(res['Account Balance']);
      const cashOnHand = Number(res['Cash On Hand (Previous EOD)']);
      const threshold = Number(res["Auto Liquidate Threshold Value"]);

      if ('Status' in res && res['Status'] != "active") {
        Swal.fire({
          title: "Account Reset Required",
          text: "You have failed one of the tests. You must Reset your account.",
          icon: 'warning',
          confirmButtonColor: '#3085d6',
          confirmButtonText: 'Reset',
          allowOutsideClick: false
        }).then((result) => {
          this.router.navigateByUrl('dashboard/billing')
        })
      } else {
        this.accountBalance.balance = accountBalance;
        this.accountBalance.pnl = accountBalance - cashOnHand;
        this.accountBalance.threshold = threshold;
      }

    })
  }

  public triggerResetMessage() {
    this._requests.postRequest("user/rithmic/disable", { user: this.user }).subscribe(res => {
      console.log(res);

      this.resetFlag = true;
    })
    // alert("Reset required");
  }

}
