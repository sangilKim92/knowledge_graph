const mongoose= require('mongoose')
const Schema = mongoose.Schema;

const driver = require('../neo4j')

const BlogSchema = new Schema({
    title: {
        type: String,
        maxlength: 128,
        required: true
    },
    content: {
        type: String
    },
    status: {
        type: String,
        required: true,
        enum: 1,
        default: 0
    },
    isPrivate: {
        type: Boolean,
        required: true,
        default: true
    },
    isSystem: {
        type: Boolean,
        required: true,
        default: false
    },
    creator: {
        type: Schema.Types.ObjectId,
        ref: 'user'
    },
    updater: {
        type: Schema.Types.ObjectId,
        ref: 'user'
    },
    createdDate: {
        type: Date,
        default: Date.now,
        required: true
    },
    updatedDate: {
        type: Date,
        default: Date.now,
        required: true
    }
});
BlogSchema.index({title: 'text'});

BlogSchema.virtual('id')
    .get(function() { return this.get('_id'); })
    .set(function(value) {return this.set('_id', value); });

BlogSchema.set('toJSON', {
    transform: function (doc, ret) {
        ret.id = ret._id;
        delete ret.__v;
    }
});

BlogSchema.pre('save', function (next) {
    const currentDate = new Date();
    this.updatedDate = currentDate;
    if (!this.createdDate) {
        this.createdDate = currentDate;
    }
    next();
});

const model = mongoose.model("blog", BlogSchema)
module.exports = model