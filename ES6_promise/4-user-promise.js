/* eslint-disable object-shorthand */
export default function signUpUser(firstName, lastName) {
  return Promise.resolve({
    firstName: firstName,
    lastName: lastName,
  });
}
