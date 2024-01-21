Feature: questionnaire
    Scenario: Questionnaire
    Given i am on SignIn Page
    When i fill in username field with username 
    And i fill in password field with password
    And i press SignIn button
    Then i should be on Home
    When i press SIM Kuesioner
    And i press Mahasiswa S1
    Then i should be on https://qa.unair.ac.id/qa/kuesioner/dashboard
    When i press Kinerja Tim Dosen
    And i press mata kuliah
    And i press DI PRAK
    And i fill form with 10
    And i press dosen
    And i chose dosen
    And i press button simpan
    And i press OK
    Then i should see Pengisian Kuesioner Berhasil
