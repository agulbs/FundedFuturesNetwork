import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule, HttpHeaders, HttpParams } from '@angular/common/http';

import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class RequestsService {
  // private url: String = "http://127.0.0.1:5000/";
  private url: String = "http://47.16.165.232:5000/";

  constructor(private http: HttpClient, private router: Router) { }

  public postRequest(url, params, user) {
    var headers;
    if ('token' in user) {
      headers = this.getHttpOptions(user);
    }

    return this.http.post(this.url + url, params, headers);
  }

  public getRequest(url, user) {
    var headers;
    if ('token' in user) {
      headers = this.getHttpOptions(user);
    }

    return this.http.get(this.url + url, headers);
  }

  public customPost(url, params) {
    return this.http.post(url, params);
  }

  public getHttpOptions(user) {
    return {
      headers: new HttpHeaders({
        "Authorization": user['token']
      })
    }
  }
}
