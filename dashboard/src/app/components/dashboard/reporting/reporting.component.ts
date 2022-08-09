import { Component, OnInit } from '@angular/core';
import { RequestsService } from '../../../services/requests.service';

@Component({
  selector: 'app-reporting',
  templateUrl: './reporting.component.html',
  styleUrls: ['./reporting.component.css']
})
export class ReportingComponent implements OnInit {

  constructor(private _requests: RequestsService) { }

  ngOnInit(): void {
    this._requests.postRequest("dashboard", {}).subscribe(res => {
      console.log(res)
    })

  }

}
