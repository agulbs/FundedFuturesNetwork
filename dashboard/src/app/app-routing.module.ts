import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomepageComponent } from './components/homepage/homepage.component';

import { LandingPageComponent } from './components/homepage/landing-page/landing-page.component';
import { AboutComponent } from './components/homepage/about/about.component';
import { PricingComponent } from './components/homepage/pricing/pricing.component';
import { SignupComponent } from './components/homepage/signup/signup.component';
import { LoginComponent } from './components/homepage/login/login.component';

import { DashboardComponent } from './components/dashboard/dashboard.component';
import { ReportingComponent } from './components/dashboard/reporting/reporting.component';

import { BillingComponent } from './components/dashboard/billing/billing.component';
import { MembershipComponent } from './components/dashboard/billing/membership/membership.component';

import { InvoiceComponent } from './components/dashboard/invoice/invoice.component';
import { ProfileComponent } from './components/dashboard/profile/profile.component';

import { AuthGuard } from './guards/auth.guard';

const routes: Routes = [

  {
    path: "", component: HomepageComponent, children: [
      { path: "", component: LandingPageComponent, },
      { path: "sign-up", component: SignupComponent, },
      { path: "login", component: LoginComponent, },
    ]
  },

  {
    path: "dashboard", component: DashboardComponent, canActivate: [AuthGuard], children: [
      { path: "", component: ReportingComponent },
      { path: "billing", component: BillingComponent },
      { path: "invoice", component: InvoiceComponent, },
      { path: "profile", component: ProfileComponent, },
    ]
  }

  // { path: "dashboard", component: DashboardComponent, pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
