import pytest

from backoffice.tests.main import client

payload = {
	"login": "lakonguina",
	"password": "password",
	"first_name": "Laury",
	"last_name": "AKONGUINA",
	"email": "lakonguina@bank.com",
	"phone": "phone",
}

@pytest.mark.run(order=1)
def test_register_user():
    response = client.post(
        "/user/register",
        json=payload,
    )

    assert response.status_code == 200
    assert response.json() == {"detail": "User created check your email for validation"}

@pytest.mark.run(order=2)
def test_register_user_email_taken():
	response = client.post(
		"/user/register",
		json=payload,
	)

	assert response.status_code == 409
	assert response.json() == {"detail": "Email is already registered and active."}

@pytest.mark.run(order=3)
def test_register_user_phone_taken():
	# Change email so previous test pass
	payload['email'] = 'lakonguina@test.com'

	response = client.post(
		"/user/register",
		json=payload,
	)

	assert response.status_code == 409
	assert response.json() == {"detail": "Phone is already registered and active."}
