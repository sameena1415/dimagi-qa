/// <reference types="cypress" />
import locator from '../../fixtures/locators.json';

class webappsPage {

    openWebapps() {
        const menu = cy.get(locator.webappsPage.webapps_menu);
        menu.click()
      }
  
    loginAs() {
        const loginas = cy.get(locator.webappsPage.loginas)
        loginas.click()
        const user = cy.get(locator.webappsPage.loginas_user)
        user.click();
        const confirm = cy.get(locator.webappsPage.confirm_user)
        confirm.click();      
    }
    
    submitForm(data1,data2,data3){
      const selectapp = cy.xpath(locator.webappsPage.select_app)
      selectapp.click()
      const selectmenu = cy.get(locator.webappsPage.select_menu);
      selectmenu.click();
      
      const openform = cy.get(locator.webappsPage.open_form)
      openform.click()
      const enterdata1 = cy.xpath(locator.webappsPage.data1_field)
      enterdata1.type(data1);
      const enterdata2 = cy.xpath(locator.webappsPage.data2_field)
      enterdata2.type(data2)
      const enterdata3 = cy.xpath(locator.webappsPage.data3_field)
      enterdata3.type(data3)
      enterdata3.click()
      const enterdata4 = cy.xpath(locator.webappsPage.data4_field)
      enterdata4.click()
      const submit = cy.get(locator.webappsPage.submit_form)
      submit.click()
      return this;          
      }

     
      
    }

  
  export default webappsPage;