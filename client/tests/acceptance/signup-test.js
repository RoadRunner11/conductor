import TestHelper from 'ember-data-factory-guy/factory-guy-test-helper';
import { test } from 'qunit';
import moduleForAcceptance from 'client/tests/helpers/module-for-acceptance';
import { authenticateSession } from 'client/tests/helpers/ember-simple-auth';

moduleForAcceptance('Acceptance | signup', {
  beforeEach() {
    TestHelper.setup();
  },

  afterEach() {
    TestHelper.teardown();
  }
});

test('visiting /signup', function(assert) {
  visit('/signup');

  andThen(function() {
    assert.equal(currentURL(), '/signup');
  });
});

test('visiting /signup when already authenticated', function(assert) {
  TestHelper.mockFindAll('student', 2);

  authenticateSession(this.application);
  visit('/signup');

  andThen(function() {
    assert.equal(currentURL(), '/dashboard');
  });
});
