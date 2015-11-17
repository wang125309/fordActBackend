var gulp = require('gulp');
var rename = require('gulp-rename');
var concat = require('gulp-concat');
var jshint = require('gulp-jshint');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var jade = require('gulp-jade');
var base64 = require('gulp-base64');
var css_minify = require('gulp-minify-css');
var browserify = require('gulp-browserify');

gulp.task('lint',function(){
    gulp.src('./static/js-modify/*.js')
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

gulp.task('sass',function(){
    gulp.src('./assets/css-modify/*.sass')
        .pipe(sass())
        .pipe(css_minify())
        .pipe(base64())
        .pipe(gulp.dest('./assets/css'));
});

var js_files = ['login','index','fullScene','share','weixin'];

gulp.task('js',function(){
    for (i in js_files) {
        gulp.src('./assets/js-modify/'+js_files[i]+'.js')
			.pipe(browserify())
			.pipe(concat('.js'))
            .pipe(gulp.dest('./assets/js'))
            .pipe(rename(js_files[i]+'.min.js'))
            .pipe(uglify())
            .pipe(gulp.dest('./assets/js'));
    }
});

gulp.task('jade',function(){
    var jade_files = {};
    gulp.src('./template/jade/*.jade')
        .pipe(jade({
            locals:jade_files
        }))
        .pipe(gulp.dest('./template/'))
});
