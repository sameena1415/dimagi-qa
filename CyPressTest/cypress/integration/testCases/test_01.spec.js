/// <reference types="cypress" />

import loginPage from '../pageObjects/loginPage'
import webappsPage from '../pageObjects/webappsPage'

describe('Formplayer Tests', function() {

    before('Login',() => { 
        const lp=new loginPage
        lp.visit()
        lp.fillEmail("automation.user.commcarehq@gmail.com")
        lp.clickContinue()
        lp.acceptCookie()
        lp.fillPassword("pass@123")
        lp.submit()
        cy.title().should('be.equal', 'CommCare HQ')})

    beforeEach(() => {
        Cypress.Cookies.preserveOnce('session_id', 'remember_token')
    })
    
    it('Open webapps', function() {        
        const lw=new webappsPage
        lw.openWebapps()
        lw.loginAs()
    })
    
    it('Submit forms', function() {    
        const sf=new webappsPage
        sf.submitForm("Woman1","Village Name1","06/10/2021")
        cy.get('#cloudcare-notifications > .alert > p').should('have.text', 'Form successfully saved!')
    })
})

