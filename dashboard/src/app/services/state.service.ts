import { Injectable } from '@angular/core';
import { Observable, Subject, BehaviorSubject } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class StateService {

  public user = {};
  public userBehavoirSubject = new BehaviorSubject<any>({});


  constructor() { }

  public setUser(user) {

    delete user['password']
    if ('token' in this.user) {
      user['token'] = this.user['token']
    }
    this.user = user;
    this.userBehavoirSubject.next(this.user);
    localStorage.setItem('ffn', JSON.stringify(user))
  }
}
