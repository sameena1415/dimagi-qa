/// <reference types="cypress" />

import loginPage from '../pageObjects/loginPage'
import webappsPage from '../pageObjects/webappsPage'
import data from '../../fixtures/userdata.json';


describe('Formplayer Tests', function() {

    before('Login',() => { 
        const lp=new loginPage
        lp.visit(Cypress.env('QA_URL'))
        lp.fillEmail(Cypress.env('LOGIN_USERNAME'))
        lp.clickContinue()
        lp.acceptCookie()
        lp.fillPassword(Cypress.env('LOGIN_PASSWORD'))
        lp.submit()
        cy.title().should('be.equal', 'CommCare HQ')})
    
    it('Open webapps', function() {        
        const lw=new webappsPage
        lw.openWebapps()
        lw.loginAs()
    })
    
    it('Submit forms', function() {    
        const sf=new webappsPage
        sf.submitForm(data.womanName,data.villageName,data.date)
        cy.get('.alert-success').should('contain.text', 'Form successfully saved!')
    })
})

