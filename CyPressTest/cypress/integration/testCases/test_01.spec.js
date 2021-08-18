/// <reference types="cypress" />

import loginPage from '../pageObjects/loginPage'
import webappsPage from '../pageObjects/webappsPage'


describe('Formplayer Tests', function() {

    before('Login',() => { 
        const lp=new loginPage
        lp.visit()
        lp.fillEmail(Cypress.env('LOGIN_USERNAME'))
        lp.clickContinue()
        lp.acceptCookie()
        lp.fillPassword(Cypress.env('LOGIN_PASSWORD'))
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
        sf.submitForm("Woman1","Village Name2","06/10/2021")
        cy.get('.alert-success').should('contain.text', 'Form successfully saved!')
    })
})

