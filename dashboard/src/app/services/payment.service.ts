import { Injectable } from '@angular/core';
import { loadStripe } from '@stripe/stripe-js';

@Injectable({
  providedIn: 'root'
})
export class PaymentService {
  private stripe = loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

  constructor() { }
}
