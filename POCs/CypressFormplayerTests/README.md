## Cypress Automation scripts

We explored Cypress to run our Formplayer tests. One can find a detailed analysis [here.](https://docs.google.com/document/d/1mdVWQack0X_mdZ-HxkCLrnhArlqk3ZCNmo0eAt-mvLE/edit)

## Executing the script

### <ins> Setting up the environment </ins>

#### Install and start local server
```sh
#### install the node_modules
npm install

#### start the local webserver
npm start
```

#### Add credentials
Create `cypress.env.json` and populate `user_name`. `user_password`. and `user_login_url`.

### <ins> Running Tests </ins>

```sh
#### To run the test
npm run cypress:open
```

