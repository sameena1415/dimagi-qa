/// <reference types="cypress" />

class logInPage {
    visit() {
      cy.visit('https://staging.commcarehq.org/accounts/login/');
    }
  
    fillEmail(value) {
      const field = cy.get('#id_auth-username');
      field.clear();
      field.type(value);
  
      return this;
    }

    acceptCookie(value) {
        const field = cy.get('#hs-eu-confirmation-button');
        field.click();

      }

      clickContinue(value) {
        const field = cy.get('.form-bubble-actions > [type="button"]');
        field.click();

      }

  
    fillPassword(value) {
      const field = cy.get('#id_auth-password');
      field.clear();
      field.type(value);
  
      return this;
    }

  
    submit() {
      const button = cy.get('.form-bubble-actions > [type="submit"]');
      button.click();
    }
  }
  
  export default logInPage;