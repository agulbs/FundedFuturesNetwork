import { FormControl, FormGroup, Validators } from '@angular/forms';

export class SignupForm {
  public static signupForm = {
    firstName: new FormControl(null, { validators: Validators.required, updateOn: 'blur' }),
    lastName: new FormControl(null, { validators: Validators.required, updateOn: 'blur' }),
    address: new FormControl(null, { validators: Validators.required, updateOn: 'blur' }),
    phone: new FormControl(null, { validators: Validators.required, updateOn: 'blur' }),
    email: new FormControl(null, { validators: Validators.required, updateOn: 'blur' }),
    username: new FormControl(null, { validators: Validators.required, updateOn: 'blur' }),
    password: new FormControl(null, { validators: Validators.required, updateOn: 'blur' }),
  }
}
