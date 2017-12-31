import { computed } from '@ember/object';
import Controller from '@ember/controller';

export default Controller.extend({
  didValidate: false,

  onSuccess() {
    this.transitionToRoute('index.student', this.get('model').student);
  },

  onFailure() {
    this.set(
      'errorMessage',
      'Huh? Something bad happened. Please contact support if it continues.');
  },

  actions: {
    create() {
      this.get('model').student.validate().then(({model, validations}) => {
        if (validations.get('isValid')) {
          model.save()
            .then(this.onSuccess.bind(this))
            .catch(this.onFailure.bind(this));
        } else {
          this.set('errorMessage', 'Oops. Something is out of whack.');
        }
        this.set('didValidate', true);
      });
    }
  },

  semestersByDate: computed('model.semesters.[]', function() {
    return this.get('model.semesters').sortBy('date');
  })
});
