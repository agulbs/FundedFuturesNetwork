import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule, HttpHeaders, HttpParams } from '@angular/common/http';

import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class RequestsService {
  private url: String = "http://127.0.0.1:5000/";

  constructor(private http: HttpClient, private router: Router) { }

  public postRequest(url, params) {
    return this.http.post(this.url + url, params);
  }
}
