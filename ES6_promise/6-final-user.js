/* eslint-disable import/extensions */
import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstname, lastname, filename) {
  return Promise.allSettled([signUpUser(firstname, lastname), uploadPhoto(filename)])
    .then((results) => 
      results.map((result) => ({
        status: result.status,
        value: result.status === 'fulfilled' ? result.value : result.reason.message,
      }))
    );
}
