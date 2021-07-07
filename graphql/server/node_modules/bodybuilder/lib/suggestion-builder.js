'use strict';

Object.defineProperty(exports, "__esModule", {
    value: true
});

var _unset2 = require('lodash/unset');

var _unset3 = _interopRequireDefault(_unset2);

var _isEmpty2 = require('lodash/isEmpty');

var _isEmpty3 = _interopRequireDefault(_isEmpty2);

exports.default = suggestionBuilder;

var _utils = require('./utils');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function suggestionBuilder(newSuggestion) {
    var suggestions = (0, _isEmpty3.default)(newSuggestion) ? {} : newSuggestion;

    function makeSuggestion(type, field) {
        var options = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : {};

        var suggestName = void 0;
        var name = options.name,
            text = options.text;


        if (name) {
            suggestName = name;
            (0, _unset3.default)(options, 'name');
        } else {
            suggestName = 'suggest_' + type + '_' + field;
        }

        var innerClause = {};

        if (text) {
            (0, _unset3.default)(options, 'text');
            innerClause.text = text;
        }

        innerClause[type] = (0, _utils.buildClause)(field, null, options);

        Object.assign(suggestions, _defineProperty({}, suggestName, innerClause));
    }

    return {
        /**
         * Add a suggestion clause to the query body.
         *
         * @param  {string}        field     Name of the field to suggest on.
         * @param  {Object}        [options] (optional) Additional options to
         *                                   include in the suggestion clause.
         *                         [options.text ] text query to run on suggest
         *                         [options.name ] pass a custom name to the function
         *                         [options.analyzer ] name of predefined analyzer to use on suggest
         * 
         * @return {bodybuilder} Builder.
         *
         * @example
         * bodybuilder()
         *   .suggest('term', price', { text: 'test' })
         *   .build()
         *
         * bodybuilder()
         *   .suggest('phrase', 'price', { text: 'test', name: 'custom name' })
         *   .build()
         *
         */
        suggest: function suggest() {
            makeSuggestion.apply(undefined, arguments);
            return this;
        },
        getSuggestions: function getSuggestions() {
            return suggestions;
        },
        hasSuggestions: function hasSuggestions() {
            return !(0, _isEmpty3.default)(suggestions);
        }
    };
}