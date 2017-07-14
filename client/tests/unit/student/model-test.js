import { moduleForModel, test } from 'ember-qunit';

moduleForModel('student', 'Unit | Model | student', {
  // Specify the other units that are required for this test.
  needs: [
    'model:school',
    'model:semester',
    'validator:number',
    'validator:presence'
  ]
});

test('it exists', function(assert) {
  let model = this.subject();
  // let store = this.store();
  assert.ok(!!model);
});

test('has a firstName', function(assert) {
  let model = this.subject();
  assert.ok(model.toJSON().hasOwnProperty('firstName'));
});

test('has a lastName', function(assert) {
  let model = this.subject();
  assert.ok(model.toJSON().hasOwnProperty('lastName'));
});

test('has a matriculationSemester', function(assert) {
  let model = this.subject();
  assert.ok(model.toJSON().hasOwnProperty('matriculationSemester'));
});

test('has many schools', function(assert) {
  let model = this.subject();
  assert.ok(model.get('schools'));
});
