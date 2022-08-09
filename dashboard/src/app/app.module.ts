import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClient, HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

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

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
