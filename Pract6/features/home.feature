Feature: Rocking with lettuce and django

   Scenario: Probando pagina Home
        Given I access the url "/home.html"
        Then I see the header "Home"

