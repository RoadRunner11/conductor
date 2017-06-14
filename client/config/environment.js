/* eslint-env node */

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'client',
    environment: environment,
    rootURL: '/',
    locationType: 'auto',

    featureFlags: {
      ENABLE_SIGNUP: false
    },
    includeDirByFlag: {
    },

    'ember-simple-auth': {
      authorizer: 'authorizer:token'
    },

    'ember-simple-auth-token': {
      refreshLeeway: 20,
    },

    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      },
      EXTEND_PROTOTYPES: {
        // Prevent Ember Data from overriding Date.parse.
        Date: false
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
    ENV.APP.API_HOST = 'https://localhost:8080';

    ENV.featureFlags.ENABLE_SIGNUP = true;

    ENV.stripe = {
      publishableKey: 'pk_test_a_fake_key'
    };
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';

    ENV.featureFlags.ENABLE_SIGNUP = true;

    ENV.stripe = {
      publishableKey: 'pk_test_a_fake_key'
    };
  }

  if (environment === 'production') {
    ENV.APP.API_HOST = process.env.API_HOST;
    ENV.rollbar = {
      accessToken: process.env.ROLLBAR_POST_CLIENT_ITEM_ACCESS_TOKEN
    };
    ENV.segment = {
      WRITE_KEY: process.env.SEGMENT_WRITE_KEY
    };
    ENV.stripe = {
      publishableKey: process.env.STRIPE_PUBLISHABLE_KEY
    };
  }

  ENV['ember-simple-auth-token'].serverTokenEndpoint = ENV.APP.API_HOST + '/api-token-auth/';
  ENV['ember-simple-auth-token'].serverTokenRefreshEndpoint = ENV.APP.API_HOST + '/api-token-refresh/';
  return ENV;
};
