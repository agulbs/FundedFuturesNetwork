import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  public user;
  public userSubject = new BehaviorSubject<any>({});

  constructor() {
    const user = localStorage.getItem('ffn');

    if (user) {
      console.log(JSON.parse(user))
      this.userSubject.next(JSON.parse(user))
    }


    this.userSubject.subscribe(user => {
      if (Object.keys(user).length > 0) {
        this.user = user;
      }
    })
  }
}
