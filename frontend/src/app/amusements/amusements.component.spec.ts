import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AmusementsComponent } from './amusements.component';

describe('AmusementsComponent', () => {
  let component: AmusementsComponent;
  let fixture: ComponentFixture<AmusementsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AmusementsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AmusementsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
