module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		sass: {
			dist: {
				files: {
					'public_html/static/css/simple-style.css': 'public_html/static/css/main.scss'
				}
			}
		},
		cssmin: {
			combine: {
				files: {
					'public_html/static/css/style.css': ['public_html/static/css/normalize.min.css', 'public_html/static/css/simple-style.css']
				}
			}
		},
		uglify: {
			js: {
				files: {
					'public_html/static/js/main.min.js': [
						'public_html/static/js/dragdivscroll-ck.js',
						'public_html/static/js/jquery.js',
						'public_html/static/js/jquery.lazyload.min.js',
						'public_html/static/js/main.js',
					]
				}
			}
		},
		watch: {
			css: {
				files: '**/*.scss',
				tasks: ['sass', 'cssmin']
			},
			js: {
				files: 'public_html/static/js/*.js',
				tasks: ['uglify']
			}
		}
	});
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-cssmin');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.registerTask('default', ['watch']);
};