import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';

import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClient, HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { GooglePlaceModule } from "ngx-google-places-autocomplete";
import { StripeModule } from "stripe-angular"



import { PricingComponent } from './components/homepage/pricing/pricing.component';
import { SignupComponent } from './components/homepage/signup/signup.component';
import { LoginComponent } from './components/homepage/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { HomepageComponent } from './components/homepage/homepage.component';
import { HomepageNavbarComponent } from './components/navbars/homepage-navbar/homepage-navbar.component';
import { DashboardNavbarComponent } from './components/navbars/dashboard-navbar/dashboard-navbar.component';
import { BillingComponent } from './components/dashboard/billing/billing.component';
import { InvoiceComponent } from './components/dashboard/invoice/invoice.component';
import { ProfileComponent } from './components/dashboard/profile/profile.component';
import { ReportingComponent } from './components/dashboard/reporting/reporting.component';
import { MembershipComponent } from './components/dashboard/billing/membership/membership.component';
import { PurchasePlanComponent } from './components/dashboard/billing/purchase-plan/purchase-plan.component';
import { AboutComponent } from './components/homepage/about/about.component';
import { StripeComponent } from './components/stripe/stripe.component';


@NgModule({
  declarations: [
    AppComponent,
    PricingComponent,
    SignupComponent,
    LoginComponent,
    DashboardComponent,
    HomepageComponent,
    HomepageNavbarComponent,
    DashboardNavbarComponent,
    BillingComponent,
    InvoiceComponent,
    ProfileComponent,
    ReportingComponent,
    MembershipComponent,
    PurchasePlanComponent,
    AboutComponent,
    StripeComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    GooglePlaceModule,
    StripeModule.forRoot("pk_test_51LVNKPKSvK2NDY9DlJ0Rk1sHelqPhWFoufs4oiglsVANLWDoDk7AaFsunqsLoGpm1kIof6Z61UPTUtxqrPSliU8w00Elkoisnb")
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
