module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		sass: {
			dist: {
				files: {
					'application/static/css/simple-style.css': 'application/static/css/base.scss'
				}
			}
		},
		cssmin: {
			combine: {
				files: {
					'application/static/css/style.css': ['application/static/css/normalize.min.css', 'application/static/css/jquery.nouislider.css', 'application/static/css/slick.css', 'application/static/css/simple-style.css']
				}
			}
		},
		uglify: {
			js: {
				files: {
					'application/static/js/main.min.js': [
						// 'application/static/js/dragdivscroll-ck.js',
						// 'application/static/js/jquery.js',
						// 'application/static/js/jquery.lazyload.min.js',
						'application/static/js/main.js',
					]
				}
			}
		},
		watch: {
			css: {
				files: ['**/*.scss', 'application/static/css/jquery.nouislider.css', 'application/static/css/slick.css'],
				tasks: ['sass', 'cssmin']
			},
			js: {
				files: 'application/static/js/main.js',
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