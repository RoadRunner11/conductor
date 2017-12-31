import Route from '@ember/routing/route';

export default Route.extend({
  queryParams: {
    search: {
      refreshModel: true
    }
  },

  model(params) {
    if (params.search.length === 0) { return null; }
    return this.store.query('school', params);
  },

  actions: {
    loading(transition) {
      let controller = this.controllerFor('index.student.find-school');
      controller.set('currentlyLoading', true);
      transition.promise.finally(function() {
          controller.set('currentlyLoading', false);
      });
    }
  },

  setupController(controller, model) {
    this._super(controller, model);
    let student = this.modelFor('index.student');
    controller.set('student', student);
  },

  resetController(controller, isExiting) {
    if (isExiting) {
      controller.set('currentlyLoading', false);
      controller.set('search', '');
    }
  }
});
