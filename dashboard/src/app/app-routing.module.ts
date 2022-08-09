import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PricingComponent } from './components/pricing/pricing.component';
import { SignupComponent } from './components/signup/signup.component';
import { LoginComponent } from './components/login/login.component';

const routes: Routes = [
  { path: "", component: PricingComponent, pathMatch: 'full' },
  { path: "sign-up", component: SignupComponent, pathMatch: 'full' },
  { path: "sign-up", component: SignupComponent, pathMatch: 'full' },
  { path: "login", component: LoginComponent, pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
