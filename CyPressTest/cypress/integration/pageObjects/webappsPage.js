/// <reference types="cypress" />

class webappsPage {

    openWebapps() {
        const menu = cy.get('#CloudcareTab > a');
        menu.click()
      }
  
    loginAs() {
        const loginas = cy.get('.js-restore-as-item')
        loginas.click()
        const user = cy.get('[aria-label="test"] > .module-column-name')
        user.click();
        const confirm = cy.get('#js-confirmation-confirm')
        confirm.click();      
    }
    
    submitForm(data1,data2,data3){
      const selectapp = cy.xpath('//*[@id="menu-region"]/div/div[2]/div[1]/div/div')
      selectapp.click()
      const selectmenu = cy.get('.module-column-name');
      selectmenu.click();
      
      const openform = cy.get('[aria-label="Registration Form"] > .module-column-name')
      openform.click()
      const enterdata1 = cy.xpath('//span[text()="Woman\'s Name English"]/following::div[1]/div[@class="widget"]/descendant::textarea')
      enterdata1.type(data1);
      const enterdata2 = cy.xpath('//span[text()="Village Name"]/following::div[1]/div[@class="widget"]/descendant::textarea')
      enterdata2.type(data2)
      const enterdata3 = cy.xpath('//span[text()="Date of Last Menstrual Period"]/following::div[1]/div[@class="widget"]/descendant::input')
      enterdata3.type(data3)
      const enterdata4 =cy.xpath('//span[text()="Date of Last Menstrual Period"]/following::div[1]/div[@class="widget"]/descendant::input')
      enterdata4.click()
      const enterdata5 =cy.xpath('//span[text()="Has the woman given birth to children that are still alive?"]/following::div[1]/div[@class="widget"]/descendant::input[@value="1"]')
      enterdata5.click()
      const submit = cy.get('.submit')
      submit.click()
      return this;          
      }

      acceptCookie() {
        const field = cy.get('#hs-eu-confirmation-button');
        field.click();
      }

    }

  
  export default webappsPage;